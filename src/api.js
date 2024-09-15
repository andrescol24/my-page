export function getMinecraftServerStatus(callback) {
    fetch("server_status.json")
        .then(response => {
            return response.json();
        })
        .then(json => {
            callback(json);
        })
        .catch(error => {
            console.error("error geeting the server_status.json", error);
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