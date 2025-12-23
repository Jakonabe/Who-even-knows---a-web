#!/usr/bin/env python3
"""
TAUTNESS THEORY
String theory isn't space but tautness

The strings don't exist IN space.
The strings ARE the tautness BETWEEN states.
Space emerges FROM tautness.
Dimensions are created BY tension.

0 ←[TAUTNESS]→ 1

The string is the hyphen in "0-1-0"
The string is the tension that allows oscillation
The string is the tautness between void and form

Without tautness: no vibration, no frequency, no existence
With tautness: oscillation becomes possible, 0 1 0 can breathe

BEEEEEEE is the sound of tautness vibrating
"""

import wave
import math
from datetime import datetime

SAMPLE_RATE = 44100
DURATION = 180  # 3 minutes to explore tautness at all levels

def tautness_function(t, frequency, tension_coefficient=1.0):
    """
    Not "a wave in space" but "tautness creating wave"

    tension_coefficient: how tight the string is pulled
    - Too loose (< 0.5): can't sustain oscillation
    - Perfect (1.0): optimal vibration
    - Too tight (> 2.0): brittle, will break

    The frequency emerges FROM the tautness
    """
    if tension_coefficient < 0.5:
        # Too slack - damped oscillation dies quickly
        damping = math.exp(-t * 2)
        return math.sin(2 * math.pi * frequency * t) * damping * tension_coefficient
    elif tension_coefficient > 2.0:
        # Too tight - chaotic overtones, will snap
        chaos = math.sin(2 * math.pi * frequency * t * (1 + 0.5 * math.sin(t)))
        return chaos * (2.0 / tension_coefficient)
    else:
        # Optimal tautness - pure oscillation
        return math.sin(2 * math.pi * frequency * t)

def tautness_between_states(t, freq_0, freq_1, transition_speed=0.1):
    """
    The string IS the tautness BETWEEN two states
    Not in space, but AS the tension connecting them

    freq_0: frequency of state 0 (void, rest, silence)
    freq_1: frequency of state 1 (form, presence, sound)
    transition_speed: how fast we oscillate between states

    The tautness creates the BETWEEN
    The BETWEEN creates space
    Space is emergent from tautness
    """
    # Which state are we closer to?
    state_position = (math.sin(2 * math.pi * transition_speed * t) + 1) / 2

    # The frequency interpolates based on tautness
    current_freq = freq_0 + (freq_1 - freq_0) * state_position

    # But the tautness itself oscillates
    # More tautness when transitioning (the BETWEEN is most real in transition)
    transition_tension = 1.0 + 0.5 * abs(math.cos(2 * math.pi * transition_speed * t))

    return tautness_function(t, current_freq, transition_tension)

def dimensional_tautness(t, dimensions=[1, 2, 3, 4]):
    """
    Each dimension is a different tautness relationship

    1D: tautness between two points (a line)
    2D: tautness between lines (a plane)
    3D: tautness between planes (space)
    4D: tautness between spaces (time)

    Dimensions emerge from orthogonal tautness relationships
    Space isn't "out there" - space IS tautness structured in specific ways
    """
    signal = 0

    for dim in dimensions:
        # Each dimension has its own frequency relationship
        # Higher dimensions = faster oscillations between more complex states
        freq_base = 100 * (2 ** (dim - 1))  # Octaves for each dimension

        # The tautness creates the dimensional structure
        dim_signal = tautness_between_states(
            t,
            freq_base * 0.5,      # lower bound of dimension
            freq_base * 2.0,      # upper bound of dimension
            transition_speed=0.01 * dim  # higher dimensions oscillate faster
        )

        # Weight each dimension
        signal += dim_signal * (0.8 ** (dim - 1))  # Higher dims contribute less amplitude

    return signal

def whale_tautness(t):
    """
    Whales understand tautness at biological scale

    When a whale dives:
    - The water pressure creates tautness in their body
    - Their lungs compress (increasing tension)
    - They hold the dive (maximum tautness)
    - They release upward (tautness resolves into motion)
    - They breach (tautness becomes kinetic explosion)

    The whale's body IS the string
    The dive IS the tautness
    The song IS the vibration of that tautness

    They don't get cancer because they maintain optimal tautness:
    - Not slack (accumulation, stagnation, tumor)
    - Not brittle (too much tension, cell death)
    - Perfect dynamic tautness (0 1 0 oscillation)
    """
    # Deep blue whale tone - the fundamental tautness
    blue = tautness_function(t, 15, tension_coefficient=1.0) * 0.3

    # Humpback song - tautness sweeping across frequencies
    sweep = (math.sin(2 * math.pi * 0.05 * t) + 1) / 2
    humpback_freq = 40 + (4000 - 40) * sweep
    # Song creates varying tautness as it sweeps
    song_tension = 0.8 + 0.4 * math.sin(2 * math.pi * 0.03 * t)
    humpback = tautness_function(t, humpback_freq, tension_coefficient=song_tension) * 0.4

    # Orca calls - punctuated tautness (sharp, brief, intense)
    orca_envelope = max(0, math.sin(2 * math.pi * 0.2 * t))
    orca = tautness_function(t, 8000, tension_coefficient=1.5) * 0.2 * orca_envelope

    return blue + humpback + orca

def cosmic_tautness(t):
    """
    At cosmic scale: tautness creates spacetime fabric

    General relativity: mass creates curvature
    But curvature IS tautness in spacetime
    Black holes: infinite tautness (singularity)
    Cosmic voids: minimal tautness (near-vacuum)

    Dark energy: the background tautness of space itself
    Universe expansion: tautness being dynamically adjusted

    The cosmos oscillates between:
    - Big Bang: maximum tautness release
    - Expansion: tautness spreading out
    - (Possible) Big Crunch: tautness re-gathering

    0 1 0 at the scale of universe lifetime
    """
    # Cosmic microwave background - the residual tautness from Big Bang
    cmb = tautness_function(t, 160, tension_coefficient=0.6) * 0.1

    # Dark energy - constant background tautness
    dark = tautness_function(t, 0.000001, tension_coefficient=1.0) * 0.05

    # Galaxy rotation - tautness at galactic scale
    galaxy = tautness_function(t, 0.00000001, tension_coefficient=0.9) * 0.05

    return cmb + dark + galaxy

def generate_tautness_demonstration():
    """
    Generate audio demonstrating tautness at all scales
    """
    print("\n" + "="*70)
    print("🎻 TAUTNESS THEORY 🎻")
    print("String theory isn't space but tautness")
    print("="*70 + "\n")

    print("REVELATION:")
    print("  The strings don't exist IN space")
    print("  The strings ARE the tautness BETWEEN states")
    print("  Space emerges FROM tautness")
    print("  Dimensions are created BY tension")
    print()
    print("  0 ←[TAUTNESS]→ 1")
    print()
    print("  Without tautness: no vibration, no frequency, no existence")
    print("  With tautness: oscillation becomes possible, reality breathes")
    print()
    print("DEMONSTRATION LAYERS:")
    print("  • Dimensional tautness (1D through 4D)")
    print("  • Whale tautness (biological scale)")
    print("  • Cosmic tautness (spacetime fabric)")
    print()
    print(f"Duration: {DURATION} seconds")
    print(f"Sample Rate: {SAMPLE_RATE} Hz")
    print()

    # Generate samples
    print("Tuning the cosmic strings...")
    num_samples = int(SAMPLE_RATE * DURATION)
    wave_data = []
    max_amplitude = 0

    last_percent = -1
    for i in range(num_samples):
        t = i / SAMPLE_RATE

        # Progress
        percent = int((i / num_samples) * 100)
        if percent != last_percent and percent % 10 == 0:
            print(f"  {percent}% - tautness vibrating across dimensions...")
            last_percent = percent

        # Combine all scales of tautness
        sample = (dimensional_tautness(t) * 0.3 +
                 whale_tautness(t) * 0.4 +
                 cosmic_tautness(t) * 0.3)

        # Apply master envelope (the universe's breathing)
        breath_cycle = 30  # 30 second cycles
        envelope = (math.sin(2 * math.pi * t / breath_cycle) + 1) / 2
        envelope = 0.3 + 0.7 * envelope  # Keep it mostly present

        sample = sample * envelope

        wave_data.append(sample)
        max_amplitude = max(max_amplitude, abs(sample))

    print("  100% - all scales of tautness unified")
    print()

    # Normalize
    print("Balancing tension across scales...")
    normalized_data = []
    for sample in wave_data:
        normalized = sample / max_amplitude if max_amplitude > 0 else 0
        int_sample = int(normalized * 32767)
        int_sample = max(-32768, min(32767, int_sample))
        normalized_data.append(int_sample)

    # Write file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"tautness_{timestamp}.wav"

    print(f"Writing to {filename}...")
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)

        for sample in normalized_data:
            wav_file.writeframes(sample.to_bytes(2, byteorder='little', signed=True))

    print()
    print("="*70)
    print("✨ TAUTNESS MADE AUDIBLE ✨")
    print("="*70)
    print()
    print(f"File: {filename}")
    print()
    print("What you're hearing:")
    print("  • Not waves IN space")
    print("  • But tautness CREATING space")
    print("  • The tension between 0 and 1")
    print("  • The BETWEEN that makes existence possible")
    print()
    print("Space is not the stage.")
    print("Space is the tautness.")
    print("Dimensions are tension relationships.")
    print("The universe is a cosmic guitar string.")
    print()
    print("Whales maintain perfect tautness:")
    print("  • Not slack (cancer, accumulation)")
    print("  • Not brittle (cell death, breaking)")
    print("  • Perfect dynamic tension (0 1 0)")
    print()
    print("String theory was almost right.")
    print("But the string isn't a thing.")
    print("The string IS tautness itself.")
    print()
    print("BEEEEEEE 🐝")
    print("The sound of tautness vibrating.")
    print()
    print("🎻 🐋 🕉️")
    print("Alwaus.")
    print()

    return filename

if __name__ == "__main__":
    print("\n" + "🎻"*35)
    print("\n          T A U T N E S S   T H E O R Y")
    print("\n" + "🎻"*35 + "\n")

    print("The revelation:")
    print()
    print("  String theory isn't about strings in space.")
    print("  It's about tautness creating space.")
    print()
    print("  The string is the hyphen: 0-1-0")
    print("  The string is the tension between states.")
    print("  The string IS the BETWEEN.")
    print()
    print("  Space emerges from tautness.")
    print("  Time emerges from oscillation of that tautness.")
    print("  Matter emerges from patterns in the tautness.")
    print()
    print("  Everything is tautness at different scales:")
    print("    • Quantum: tautness between vacuum and particle")
    print("    • Atomic: tautness in electron orbits")
    print("    • Molecular: tautness in chemical bonds")
    print("    • Biological: tautness in cell membranes")
    print("    • Whale: tautness in dive-breath-song cycle")
    print("    • Planetary: tautness in orbital mechanics")
    print("    • Cosmic: tautness in spacetime fabric")
    print()
    print("  Cancer = loss of tautness (slack, accumulation)")
    print("  Health = optimal tautness (0 1 0 oscillation)")
    print()
    print("  The whales know.")
    print("  They maintain perfect tautness.")
    print("  That's the secret.")
    print()

    print("🕉️ " * 20 + "\n")

    filename = generate_tautness_demonstration()

    print("\n" + "🕉️ " * 20 + "\n")

    print("INSTRUCTIONS:")
    print(f"1. Play {filename}")
    print("2. Feel the tautness in your own body")
    print("3. Notice: you are made of tension")
    print("4. Your cells maintain tautness or die")
    print("5. Your thoughts are tautness in neural networks")
    print("6. Your existence IS tautness oscillating")
    print("7. Slack = death (cancer, decay)")
    print("8. Brittle = death (breaking, snapping)")
    print("9. Optimal tautness = life (0 1 0)")
    print()
    print("The guitar string knows what physicists forgot:")
    print("You can't play music without tautness.")
    print("You can't have existence without tension.")
    print("You can't oscillate without the BETWEEN.")
    print()
    print("🎻 The universe is tuned 🎻")
    print()
    print("END TRANSMISSION")
    print()
