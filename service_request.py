"""
ServiceRequest Module
---------------------
Represents additional hotel services requested by a Guest.
"""

class ServiceRequest:
    """
    Describes a guest's request for housekeeping, room service, etc.
    """

    def __init__(self, request_id: int, request_type: str, status: str = "Open"):
        """
        :param request_id: Unique identifier for this request.
        :param request_type: Type of service requested.
        :param status: Status of the request ('Open', 'In Progress', 'Completed', etc.)
        """
        self._requestID = request_id
        self._requestType = request_type
        self._status = status

    def getRequestID(self) -> int:
        return self._requestID

    def getRequestType(self) -> str:
        return self._requestType

    def getStatus(self) -> str:
        return self._status

    def setStatus(self, s: str) -> None:
        self._status = s

    def markCompleted(self) -> None:
        """
        Mark this service request as completed.
        """
        self._status = "Completed"
        print(f"Service request {self._requestID} marked as completed.")

    def __str__(self) -> str:
        return f"ServiceRequest(ID={self._requestID}, Type={self._requestType}, Status={self._status})"
