## Overview

This packages the main branch of [SEMAFOR](http://www.cs.cmu.edu/~ark/SEMAFOR/) into a set of docker containers.  SEMAFOR is a frame-semantic parser developed by Dipanjan Das, Sam Thomson, Meghana Kshirsagar, André F. T. Martins, Nathan Schneider, Desai Chen, and Noah Smith. Open-source software developed for research purposes, SEMAFOR automatically processes English sentences according to the form of semantic analysis in Berkeley FrameNet.

## Containers

There are three containers:

* semafor-base:  Builds the JAR from the SEMAFOR 3.0 alpha main branch using Maven.  The other containers are both based on this image.
* semafor-frameparser:  Runs the frame extraction server.
* semafor-api:  A Flask web service that accepts a body of text via HTTP POST and returns it's JSON representation of marked-up frames.  It also performs some text pre-processing, first applies the NLTK Punkt sentence tokenizer to each line, and then the MaltParser for syntactic dependencies.

To pull the images:

```
$ docker pull reutersmedia/semafor-frameparser:latest
$ docker pull reutersmedia/semafor-api:latest
```

## Running

A docker-compose YAML file is provided, and is the easiest way to deploy.  Download the file locally and run:

```
cd docker-compose/semafor-svr
docker-compose up -d
```

This will launch two linked containers, one with the API, and one with the frame parser.  To use:

```
curl -X POST -d @myfile "http://localhost:8080/parse-frames"
```

As a convience, you can also pass short text fragments via an HTTP GET:

```
curl "http://localhost:8080/parse-frames?t=The+moon+is+made+of+cheese."
```

## Copyright

Copyright (C) 2017 Thomson Reuters

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.