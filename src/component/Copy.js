import { Button, OverlayTrigger, Popover } from 'react-bootstrap';

export default function Copy ({text}) {
    const copyValue = () => {
        navigator.clipboard.writeText(text);
    };
    const showPopover = (
        <Popover id="popover-positioned-bottom" title="Copiado!">
            IP copiada! <strong>Puede cambiar luego</strong>
        </Popover>
    );
    return (
        <OverlayTrigger trigger="click" placement='bottom' overlay={showPopover}>
            <Button onClick={copyValue}>{text}</Button>
        </OverlayTrigger>
    
);
}