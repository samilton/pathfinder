# OpenAI Integration Documentation

```{mermaid}

   sequenceDiagram
       participant Mattermost
       participant Mattermost Server
       participant Pathfinder
       participant OpenAI

       Mattermost->>Mattermost Server: Help me?!
       Mattermost Server->>Pathfinder: Help me?!
       Pathfinder->>OpenAI: Help me?!
       OpenAI->>Pathfinder: As an AI assistant, how can i help?
```

```python

    import OpenAI

    oai = OpenAI()
```

