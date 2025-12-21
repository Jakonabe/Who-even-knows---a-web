#!/usr/bin/env python3
"""
GREAT VIBES GENERATOR
The philosophy becomes executable frequency
0 1 0 - oscillation as code
BEEEEEEE
"""

import wave
import math
from datetime import datetime

# CONSTANTS (the sacred frequencies)
SAMPLE_RATE = 44100  # Hz
DURATION = 108  # seconds (sacred number: 1+0+8=9, reduction to unity)

# Whale frequencies (infrasound to ultrasound)
FREQUENCIES = {
    'blue_whale': 15,      # Hz - the deep breath
    'humpback_low': 40,    # Hz - the song begins
    'humpback_high': 4000, # Hz - the song peaks
    'orca': 12000,         # Hz - the family speaks
    'heartbeat': 1.2,      # Hz - ubuntu pulse (72 bpm)
}

def oscillate(t, freq, phase=0):
    """
    Pure oscillation: sin wave
    The mathematical embodiment of 0 1 0
    """
    return math.sin(2 * math.pi * freq * t + phase)

def jettison_envelope(t, duration, breath_length=4):
    """
    0 1 0 pattern as amplitude envelope
    inhale (rise) -> hold (sustain) -> exhale (fall) -> silence (rest)
    """
    cycle_position = (t % breath_length) / breath_length

    if cycle_position < 0.3:  # inhale (1 rising)
        return cycle_position / 0.3
    elif cycle_position < 0.5:  # hold (1 sustained)
        return 1.0
    elif cycle_position < 0.8:  # exhale (0 falling)
        return 1.0 - ((cycle_position - 0.5) / 0.3)
    else:  # silence (0 rest)
        return 0.0

def whale_song(t):
    """
    Composite frequency: multiple whales singing together
    Ubuntu at the frequency level
    """
    # Base drone (blue whale depth)
    base = oscillate(t, FREQUENCIES['blue_whale']) * 0.3

    # Humpback melody (oscillating between low and high)
    melody_freq = FREQUENCIES['humpback_low'] + (
        (FREQUENCIES['humpback_high'] - FREQUENCIES['humpback_low']) *
        (math.sin(2 * math.pi * 0.05 * t) + 1) / 2  # slowly sweep frequencies
    )
    melody = oscillate(t, melody_freq) * 0.4

    # Heartbeat pulse (ubuntu)
    heartbeat = oscillate(t, FREQUENCIES['heartbeat']) * 0.2

    # Orca punctuation (the family responds)
    orca = oscillate(t, FREQUENCIES['orca'], phase=t) * 0.1 * math.sin(2 * math.pi * 0.2 * t)

    return base + melody + heartbeat + orca

def generate_great_vibes():
    """
    THE MAIN FUNCTION
    Generates the audio file: philosophy as vibration
    """
    print("🐋 GENERATING GREAT VIBES 🐋")
    print(f"Duration: {DURATION} seconds")
    print(f"Sample Rate: {SAMPLE_RATE} Hz")
    print("Frequencies: AAT ALL FREQUENCIES")
    print()
    print("0 1 0 1 0 1 0 1 0 1 0 1 0")
    print()

    # Generate the composite wave sample by sample
    print("Jettisoning vibrations...")
    num_samples = int(SAMPLE_RATE * DURATION)
    wave_data = []
    max_amplitude = 0

    for i in range(num_samples):
        t = i / SAMPLE_RATE

        # Generate whale song
        sample = whale_song(t)

        # Apply breathing envelope (0 1 0 pattern)
        envelope = jettison_envelope(t, DURATION, breath_length=8)
        sample = sample * envelope

        wave_data.append(sample)
        max_amplitude = max(max_amplitude, abs(sample))

    # Normalize to prevent clipping and convert to 16-bit integers
    print("Applying oscillation envelope...")
    normalized_data = []
    for sample in wave_data:
        normalized = sample / max_amplitude if max_amplitude > 0 else 0
        int_sample = int(normalized * 32767)
        # Clamp to 16-bit range
        int_sample = max(-32768, min(32767, int_sample))
        normalized_data.append(int_sample)

    # Write to WAV file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"great_vibes_{timestamp}.wav"

    print(f"Writing to {filename}...")
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(SAMPLE_RATE)

        # Write samples
        for sample in normalized_data:
            wav_file.writeframes(sample.to_bytes(2, byteorder='little', signed=True))

    print()
    print("✨ GREAT VIBES GENERATED ✨")
    print(f"File: {filename}")
    print()
    print("The philosophy is now sound.")
    print("The frequency is truth.")
    print("0 1 0 = LIFE")
    print()
    print("BEEEEEEE 🐝")
    print("AAT ALL FREQUENCIES 🕉️")
    print()
    print("Alwaus.")

    return filename

def print_the_pattern():
    """
    Visual oscillation in terminal
    """
    print("\n" + "="*50)
    print("THE PATTERN THAT MAKES PRESENCE POSSIBLE THROUGH ABSENCE")
    print("="*50 + "\n")

    for i in range(5):
        print("0 " * 20)
        print("  1 " * 18)
        print("    0 " * 16)
        print("      1 " * 14)
        print("        0 " * 12)
        print()

    print("JETTISONING → OSCILLATION → LIFE")
    print("ACCUMULATION → STAGNATION → DEATH")
    print()
    print("The whales know.")
    print("BEEEEEEE 🐋")
    print()

if __name__ == "__main__":
    print_the_pattern()

    print("\n" + "🕉️ "*20 + "\n")

    # Generate the vibes
    filename = generate_great_vibes()

    print("\n" + "🕉️ "*20 + "\n")

    print("INSTRUCTIONS:")
    print(f"1. Play {filename}")
    print("2. Close your eyes")
    print("3. Breathe with the oscillation")
    print("4. Jettison")
    print("5. BEEEEEEE")
    print()
    print("🐋 🐋 🐋 🐋 🐋 🐋 🐋 🐋 🐋")
    print()
    print("END TRANSMISSION")
    print()
