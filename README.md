# EduCare-Multi-Agent-System
EduCare is a multi-agent learning system that creates personalized study plans, evaluates progress with quizzes, and tracks student well-being. Using Gemini, custom tools, and a shared memory bank, it adapts over time to help learners study smarter and maintain balance.
Project Overview — EduCare

NOTE: This is a sample-style project overview for the Kaggle Agents Intensive Capstone Project. It follows the structure demonstrated in the official ADK sample submissions but contains fully original logic tailored to EduCare.

Project Overview

This project implements EduCare, a multi-agent system designed to support students through personalized study planning, progress evaluation, and well-being monitoring. Built with the Google Agent Development Kit (ADK), EduCare demonstrates how AI agents can help learners stay organized, avoid burnout, and receive adaptive guidance throughout their academic schedule.

The system blends LLM reasoning, memory-based personalization, custom tools, and parallel orchestration to deliver a seamless study companion.

Problem Statement

Students often struggle with inconsistent study habits, unclear planning, and frequent academic burnout. Keeping track of deadlines, deciding what to study next, and measuring progress require sustained effort. On top of that, many students overlook their mental well-being until stress becomes unmanageable.

Traditional study planners are static. They don’t adapt. They don’t respond to fatigue, changing priorities, or learning progress. As a result, students lose momentum, fall behind, and experience compounded stress.

Solution Statement

EduCare introduces a multi-agent, adaptive learning support system that removes the friction from study management. Agents work together to:

Generate personalized and dynamic study plans

Evaluate learning through quick quizzes

Track emotional well-being through light daily check-ins

Store session history in a memory bank to improve over time

By coordinating these capabilities, EduCare creates a balanced structure that keeps learners on track academically and mentally.

Architecture

At the core of EduCare is the interactive_study_coach, an orchestrator that coordinates specialized sub-agents. EduCare is not a single model; it’s a structured ecosystem enabled by the ADK, featuring:

Study Planner (Gemini-powered)

A LoopAgent that constructs realistic, personalized study plans. It uses memory to adjust plans based on prior performance, fatigue signals, and upcoming deadlines.

Evaluator Agent

Generates short quizzes, grades responses, and provides targeted feedback. Uses a validation checker to ensure quizzes match difficulty and topic coverage.

Wellness Check Agent

Runs in parallel, prompting quick mental-health check-ins and adjusting workload recommendations to prevent burnout.

Memory & Tools

Memory Bank: Tracks past plans, quiz results, and wellness patterns

Custom Tools: Store reports, track progress, and log well-being signals

Observability hooks: Logging + metrics for debugging and evaluation

Conclusion

EduCare shows how multi-agent systems can meaningfully support learners beyond simple chat interactions. By distributing responsibilities across specialized agents and coordinating them through the ADK, EduCare delivers a study experience that’s adaptive, efficient, and mindful of student well-being.

If extended further, EduCare could integrate calendar syncing, study streak tracking, and real-time difficulty adjustment based on long-term learning patterns.
