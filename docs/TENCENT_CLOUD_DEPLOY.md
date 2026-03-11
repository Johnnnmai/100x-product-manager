# Tencent Cloud Deployment

## Goal

Deploy one long-running control console service to Tencent Cloud without changing the existing `GitHub -> OpenClaw` worker path.

## What Gets Deployed

- FastAPI control console: `ai_os.web`
- Existing repo-mounted `ops/` directories for task, approval, and report state
- No replacement of the current OpenClaw cloud worker

## Local Run

```bash
python -m pip install -e .
npm run ui:start
```

Open:

```text
http://localhost:8080
```

## Docker Build

```bash
docker build -t company-ai-os-console .
docker run --rm -p 8080:8080 --env-file .env company-ai-os-console
```

Open:

```text
http://<server-ip>:8080
```

## Tencent Cloud CVM Deploy

On the server:

```bash
git clone <your-repo-url> company-ai-os
cd company-ai-os
cp .env.example .env
docker build -t company-ai-os-console .
docker run -d \
  --name company-ai-os-console \
  --restart unless-stopped \
  -p 8080:8080 \
  --env-file .env \
  company-ai-os-console
```

## Required Env Vars

- `PAPERCLIP_COMPANY_ID`
- `DISCORD_BOT_TOKEN`
- `DISCORD_CHANNEL_ID`
- `GITHUB_ORG_NAME`
- `GITHUB_BROWSER_PROFILE_DIR`

## Production Notes

- Keep the console and OpenClaw in the same repo or shared volume view of `ops/`.
- Do not expose the service publicly without a fronting auth layer or private network.
- Use Tencent security groups to allow only trusted source IPs to port `8080`.
- The console is an operator surface; real cloud execution still happens in OpenClaw.
