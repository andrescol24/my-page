import { useEffect, useState } from "react";
import "./MinecraftPage.css"
import { getMinecraftServerStatus } from "../api.js";
import Copy from "../component/Copy.js";
import StartServerFormulary from "../component/StartServerFormulary.js";

function MinecraftPage() {
    const [serverStatus, setServerStatus] = useState({ip: null, running: false});
    
    useEffect(() => {
        getMinecraftServerStatus(setServerStatus);
    }, []);
    
    return (
        <>
            <div>
                <h1 className="text-center">Servidor de amigos que no pelean</h1>
                    {serverStatus.running 
                        ? <p id="ip" className="text-center">
                            <span>Puedes copiar la IP aquí: </span>
                            <Copy text={serverStatus.ip}/>
                            </p>
                        : <StartServerFormulary updateStatus={setServerStatus}/>
                    }
            </div>
        </>
    );
}
export default MinecraftPage;