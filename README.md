# Face Transform for Dify: step-by-step guide

Analyze facial keypoints in an authorized image. This guide takes you from your first API key to the result in a Dify Workflow. Screenshots use Dify CE 1.17.1 in English; later versions may move the same controls.

[Read in Simplified Chinese](https://github.com/AceDataCloud/FaceDify/blob/main/readme/README_zh_Hans.md) · [API and pricing](https://platform.acedata.cloud/models)

## 1. Install the correct plugin

Open [Face Transform by acedatacloud](https://marketplace.dify.ai/plugin/acedatacloud/face) in Dify Marketplace. Check the author is **acedatacloud**, choose **Install**, and select your Dify workspace. In your Dify workspace, open **Integrations → Tools → Tool Plugin** and select **Face Transform**. Its card should say **From Marketplace**.

If your Dify server cannot open Marketplace, ask its administrator to enable outbound access and plugin installation. The plugin needs HTTPS to `api.acedata.cloud`.

![Installed plugin in Dify](https://raw.githubusercontent.com/AceDataCloud/FaceDify/887fa46ee37d554be8e0be94f37d7413464e894c/_assets/tutorial/01-installed.png)

## 2. Get an API key with the correct access

1. Sign in at [Ace Data Cloud → Applications](https://platform.acedata.cloud/console/applications).
2. Open **General application**. Its API key can access multiple services your account is entitled to use. A service-specific key is limited to that service. For this tutorial, check **Face Transform** access and current pricing/balance before generating.
3. To reuse the selected key, click the copy icon marked **1** below. To create a separate Dify key, click **Manage Keys** marked **2**, then **Create**.

![Copy an existing API key or open Manage Keys](https://raw.githubusercontent.com/AceDataCloud/FaceDify/887fa46ee37d554be8e0be94f37d7413464e894c/_assets/tutorial/get-api-key-en.png)

4. Give the new key a name, such as `Dify tutorial`. Set expiration and usage/API restrictions only as needed, then click **Create**. Return to the key list or application card and copy the key. If **Allowed APIs** is enabled, include the synchronous API used here: `/face/analyze`.

![Create an optional separate key](https://raw.githubusercontent.com/AceDataCloud/FaceDify/887fa46ee37d554be8e0be94f37d7413464e894c/_assets/tutorial/create-api-key-en.png)

Copy only the token string. Do not add `Bearer `, quotation marks, or the screenshot's redacted characters. A platform management token (for example, a `platform-...` token) is not the generation API key this plugin expects. Confirm service access and a sufficient balance before the first run.

## 3. Authorize Face Transform in Dify

1. Open **Integrations → Tools → Tool Plugin → Face Transform**.
2. Click **API Key Authorization Configuration**. If an authorization already exists, click **1 Authorization** first, then the configuration button.
3. Enter an **Authorization Name**, such as `Ace Data Cloud`, and paste the copied token into **Ace Data Cloud Bearer Token**.
4. Choose who may use the credential and click **Save**. Never put a key in a prompt or workflow export.

![Dify tool authorization dialog](https://raw.githubusercontent.com/AceDataCloud/FaceDify/887fa46ee37d554be8e0be94f37d7413464e894c/_assets/tutorial/02-authorize.png)

## 4. Build your first Workflow

Open **Studio → Create → Create from Blank → Workflow**, name it, and create this path by dragging from each node's right connector to the next node:

**Start → Face Transform → Output**.

Use the **+** button to add a **Tool**, select this plugin, and choose the exact action above. Rename the tool node **Face Transform** to match the screenshots. Leave Start inputs empty for this fixed first example. Keep **Retry on Failure** off on the generation node.

![Workflow connections](https://raw.githubusercontent.com/AceDataCloud/FaceDify/887fa46ee37d554be8e0be94f37d7413464e894c/_assets/tutorial/03-workflow.png)

Select **Face Transform** and set these fields. Leave unmentioned optional fields empty.

| Dify field | First-run value |
|---|---|
| Action (`action`) | `keypoints` |
| Analyze Mode (`mode`) | `1` |

**Image URL** (`image_url`):

```text
https://platform2.cdn.acedata.cloud/seedream/00355681-7e81-49a4-a8fc-d2165fe1e9fd.jpg
```

This example only analyzes keypoints with **Action** `keypoints`; it does not change the face. Use your own authorized image URL. The pictured fictional portrait is a previously generated test image.

![Fill the generation or search parameters](https://raw.githubusercontent.com/AceDataCloud/FaceDify/887fa46ee37d554be8e0be94f37d7413464e894c/_assets/tutorial/03-configure.png)

## 5. Return the synchronous result

Add an **Output** node and map `status` to **Face Transform → status**, `success` to **Face Transform → success**, and `data` to **Face Transform → data**. No task-query or waiting node is required. Click **Test Run → Start Run**. Inspect the returned structured face-analysis data. An input with no detectable face may return empty analysis instead of an image.

![Synchronous output mapping](https://raw.githubusercontent.com/AceDataCloud/FaceDify/887fa46ee37d554be8e0be94f37d7413464e894c/_assets/tutorial/05-output.png)

## 6. Check the expected output

A completed result has this shape (the URL below illustrates the field; use your own returned URL):

```json
{
  "status": "succeeded",
  "success": true,
  "data": {
    "face_shape_set": [],
    "image_width": 1024,
    "image_height": 1024
  }
}
```

![Actual completed Dify result](https://raw.githubusercontent.com/AceDataCloud/FaceDify/887fa46ee37d554be8e0be94f37d7413464e894c/_assets/tutorial/06-result.png)

Actual run example; your task ID and media URL will differ.

## Troubleshooting

| What you see | What to do |
|---|---|
| Authorization fails / 401 or 403 | Copy the full API token, remove `Bearer `, check service access, balance, expiration and Allowed APIs. |
| Invalid parameter / 400 | Copy the exact example model, action, resolution and JSON shape. Do not combine unrelated action fields. |
| HTTP 429 | Wait, reduce concurrency and check service limits; do not enable automatic paid retries. |
| Timeout / 5xx / failed task | Inspect the original task or request history before resubmitting. Contact support with task/trace ID, never your key. |

[Download the ready-to-import workflow](https://github.com/AceDataCloud/FaceDify/raw/refs/heads/main/docs/quickstart.dify.yml). Import it in Studio, then configure your own key; the file contains no credentials.

## Privacy, cost and support

The free plugin sends your chosen inputs and token to `api.acedata.cloud`; API calls follow current service pricing. Keys stay in Dify credential storage. See [Privacy](https://github.com/AceDataCloud/FaceDify/blob/main/PRIVACY.md). Only submit content you have permission to process.

[Source](https://github.com/AceDataCloud/FaceDify) · [Report a problem](https://github.com/AceDataCloud/FaceDify/issues) · dev@acedata.cloud · [Advanced capabilities](https://github.com/AceDataCloud/FaceDify/blob/main/CAPABILITIES.md). Development and test evidence live in the source repository, separate from this first-run guide.
