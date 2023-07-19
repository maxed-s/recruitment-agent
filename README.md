# recruitment-agent
Current goal is to integrate some sort of LLM framework (had started with LangChain but am leaning towards GripTape) to create a recruiting agent. 

The agent should be able to parse a job opening as inputted from a hiring manager (e.g. "software engineer needed for SaaS product") and break it down into what qualifications are needed. Should then take that information -> create a job posting from that info. Then it should scour LinkedIn and find matching profiles. 

Would be ideal if it was able to "chat" with PDFs (eval. PDFs of resumes sent by candidates to understand whether they're qualified). That is, however, a separate goal that can be accomplished later. 

Current focus is integrating GripTape. 
