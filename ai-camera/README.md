# Setup Home

## Create home cluster in the cloud

Create cluster using exp version of fluvio

```
$  fluvio cloud cluster create mldemo --version 0.13.0-dev-2
```

## Set up as home and register edges

```
$ fluvio remote register edge1 
```

## Create topics related to edge1

We are going to create two topic.

`input-label` to send to edge1

```
$ fluvio topic create input-labels --mirror-apply mirror.json --home-to-remote
```

`output-labels` to receive from edge1

```
$ fluvio --profile topic create output-labels --mirror-apply mirror.json
```

## Export edge configuration

```
$ fluvio cloud remote export edge1  --file edge1-home.json
```

The file `edge1-home.json` need to be copied to edge

# Edge Configuration