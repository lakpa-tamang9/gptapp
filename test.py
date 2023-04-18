import replicate


prompt = {"prompt": "a vision of paradise. unreal engine"}
output = replicate.run(
    "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
    input=prompt,
)
print(output[0].url)
