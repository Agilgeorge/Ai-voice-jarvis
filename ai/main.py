import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe,JobContext,WorkerOptions,cli,llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai,silero
load_dotenv()
async def entrypoint(ctx: JobContext):
    initial_ctx=lim.chatContext().append(
        role="system",
        text=(
            "you are a voice assistant created by livekit."
        )
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    assistant = VoiceAssistant(
        vad=silero.vad.load(),
        stt = openai.STT(),
        llm = openai.llm(),
        tts=openai.TTS(),
        chat_ctx=initial_ctx,
    )
    assistant.start(ctx.room)
    await asyncio.sleep(1)
    await assistant.say("hey,how about a help",allow_interruptions=True)

if __name__== "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))