export function getMinecraftServerStatus(callback) {
    fetch("https://pqwhdog7ohjr4siqooioddkcg40vftnv.lambda-url.us-east-1.on.aws")
        .then(response => {
            return response.json();
        })
        .then(json => {
            callback(json);
        })
        .catch(error => {
            console.error("error geeting the server status", error);
        });
}

export function startMinecraftServer(userInformation, success, errorCallback) {
    fetch("https://lpk5bigz3tlomyxkhvnqmcs2sa0qmjeb.lambda-url.us-east-1.on.aws", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({user: userInformation.user, password: userInformation.password})
    }).then(response => {
        return response.json()
    }).then(json => {
        success(json)
    }).catch(error => {
        errorCallback(error);
    })
}