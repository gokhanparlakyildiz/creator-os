# Trend Agent

The Trend Agent turns normalized signals from an external source into ranked
content opportunities.

## First iteration

1. A `TrendSource` fetches candidates for a creator niche.
2. Each candidate reports relevance, velocity, and engagement from 0.0 to 1.0.
3. `TrendAgent` calculates a transparent weighted score:

```text
score = relevance × 0.50 + velocity × 0.30 + engagement × 0.20
```

4. The strongest candidates are returned first.

The source is deliberately an interface. Live integrations can be added later
without coupling ranking rules to a particular API.
